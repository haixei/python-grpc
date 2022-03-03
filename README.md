# gRPC Overview in Python
This repository contains a simple example of a gRPC implementation. For more information about this project in particular visit this article (Basics of gRPC with Python) or the technology's website.

## About the example
In this repository you will find some auto-generated files as well as our client, server and most importantly - the proto file. This simple example shows how to create routes for a café's menu and how to use them.

## Run the project
To run the project you need to make sure that you have installed the required packages, all defined in the requirements.txt file.
1. Start with:
    ```shell
    pip install -r requirements.txt
    ```
   
2. Next, you will need two terminals, one for the server and another one for the client. Then run:
   ```shell
    pip cafe_server.py
    ```
   ```shell
    pip cafe_client.py
    ```


### Useful resources
- [*Official introduction to gRPC*](https://grpc.io/docs/what-is-grpc/introduction/)
- [*Google on protocol buffers*](https://developers.google.com/protocol-buffers/docs/overview)
- [*Google on Python generated code*](https://developers.google.com/protocol-buffers/docs/reference/python-generated)