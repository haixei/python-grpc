"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import cafe_pb2
import cafe_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = cafe_pb2_grpc.MenuStub(channel)
        response = stub.SpecialOfTheDay(cafe_pb2.Weekday(weekday=1))
    print(response)


if __name__ == '__main__':
    logging.basicConfig()
    run()
