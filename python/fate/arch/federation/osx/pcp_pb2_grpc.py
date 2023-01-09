# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
import pcp_pb2 as pcp__pb2


class PrivateTransferProtocolStub(object):
    """互联互通如果使用异步传输协议作为标准参考，Header会复用metadata传输互联互通协议报头，且metadata中会传输异步场景下的消息相关属性
    互联互通如果使用其他协议作为参考标准，Header会复用metadata传输互联互通协议报头
    互联互通如果使用GRPC作为参考标准，Header会复用HTTP2的报头传输互联互通协议报头

    service PPCTransferService {
    rpc push (stream Inbound) returns (Outbound);
    //  rpc pull (Metadata) returns (stream Packet);
    rpc unaryCall (Inbound) returns (Outbound);
    // rpc polling (stream PollingFrame) returns (stream PollingFrame);




    }

    """

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.transport = channel.stream_stream(
            "/org.ppc.ptp.PrivateTransferProtocol/transport",
            request_serializer=pcp__pb2.Inbound.SerializeToString,
            response_deserializer=pcp__pb2.Outbound.FromString,
        )
        self.invoke = channel.unary_unary(
            "/org.ppc.ptp.PrivateTransferProtocol/invoke",
            request_serializer=pcp__pb2.Inbound.SerializeToString,
            response_deserializer=pcp__pb2.Outbound.FromString,
        )


class PrivateTransferProtocolServicer(object):
    """互联互通如果使用异步传输协议作为标准参考，Header会复用metadata传输互联互通协议报头，且metadata中会传输异步场景下的消息相关属性
    互联互通如果使用其他协议作为参考标准，Header会复用metadata传输互联互通协议报头
    互联互通如果使用GRPC作为参考标准，Header会复用HTTP2的报头传输互联互通协议报头

    service PPCTransferService {
    rpc push (stream Inbound) returns (Outbound);
    //  rpc pull (Metadata) returns (stream Packet);
    rpc unaryCall (Inbound) returns (Outbound);
    // rpc polling (stream PollingFrame) returns (stream PollingFrame);




    }

    """

    def transport(self, request_iterator, context):
        # missing associated documentation comment in .proto file
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def invoke(self, request, context):
        # missing associated documentation comment in .proto file
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PrivateTransferProtocolServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "transport": grpc.stream_stream_rpc_method_handler(
            servicer.transport,
            request_deserializer=pcp__pb2.Inbound.FromString,
            response_serializer=pcp__pb2.Outbound.SerializeToString,
        ),
        "invoke": grpc.unary_unary_rpc_method_handler(
            servicer.invoke,
            request_deserializer=pcp__pb2.Inbound.FromString,
            response_serializer=pcp__pb2.Outbound.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("org.ppc.ptp.PrivateTransferProtocol", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))