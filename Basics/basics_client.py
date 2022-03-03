from __future__ import print_function

import logging

import grpc
import basics_pb2
import basics_pb2_grpc


# Test the Hello route
def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = basics_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(basics_pb2.HelloRequest(name='Claire'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
