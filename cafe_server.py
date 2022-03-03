from concurrent import futures
import logging

import grpc
import cafe_pb2
import cafe_pb2_grpc
import pandas as pd

# Open the CSV with menu items
data = pd.read_csv("./data/menu.csv")
print(data.shape)


class Cafe(cafe_pb2_grpc.MenuServicer):

    # Get product information
    def Pricing(self, request, context):
        product = data.loc[data['Menu Items'] == request.product]

        # If the product doesn't exist, return an error with a message
        if len(product) == 0:
            available_products = data['Menu Items']
            context.set_details = 'This product does not exist. Select one of these: ' + ', '.join(available_products)
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return cafe_pb2.ProductInfo()

        # If found, return the product information
        return cafe_pb2.ProductInfo(product=product['Menu Items'].item(), price=product['Price'].item(),
                                    flavors=product['Flavors'].item(), availability=product['Availability'].item())

    # Return the drink of the day
    def SpecialOfTheDay(self, request, context):
        drinks = data.loc[data['Type'] == 'Drink']

        # Select randomly from the drinks
        drink_of_the_day = drinks.sample(n=1)

        # Drink of the day always costs only 75% of the original price
        return cafe_pb2.SpecialDrink(product=drink_of_the_day['Menu Items'].item(),
                                     special_price=round(drink_of_the_day['Price'].item() * 0.75))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cafe_pb2_grpc.add_MenuServicer_to_server(Cafe(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
