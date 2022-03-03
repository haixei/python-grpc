![Status: Finished](https://img.shields.io/badge/Status-Finished-%235d6d91)
# gRPC Overview in Python
This repository contains a simple example of a gRPC implementation. For more information about this project in particular visit the gRPC's website.

## About the example
 I divided the projects into sub-folders in case I will do more tests later, so far the repository consists of the "basics" and the "café". The first one was following the example from the documentation, the latter is an expanded version of it that I build while trying out the features. Both are a unary RPC. In their folders you will find some auto-generated files as well as our client, server and most importantly - the proto file.

## Run the project
To run the project you need to make sure that you have installed the required packages, all defined in the requirements.txt file.
1. Start with:
    ```shell
    pip install -r requirements.txt
    ```
   
2. Next, you will need two terminals, one for the server and another one for the client. Then run:
   ```shell
    python <project name>_server.py
    ```
   ```shell
    python <project name>_client.py
    ```



### Useful resources
- [*Official introduction to gRPC*](https://grpc.io/docs/what-is-grpc/introduction/)
- [*Google on protocol buffers*](https://developers.google.com/protocol-buffers/docs/overview)
- [*Google on Python generated code*](https://developers.google.com/protocol-buffers/docs/reference/python-generated)