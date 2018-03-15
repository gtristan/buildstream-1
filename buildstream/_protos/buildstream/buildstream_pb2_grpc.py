# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from buildstream._protos.buildstream import buildstream_pb2 as buildstream_dot_buildstream__pb2


class ArtifactCacheStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetArtifact = channel.unary_unary(
        '/buildstream.ArtifactCache/GetArtifact',
        request_serializer=buildstream_dot_buildstream__pb2.GetArtifactRequest.SerializeToString,
        response_deserializer=buildstream_dot_buildstream__pb2.GetArtifactResponse.FromString,
        )
    self.UpdateArtifact = channel.unary_unary(
        '/buildstream.ArtifactCache/UpdateArtifact',
        request_serializer=buildstream_dot_buildstream__pb2.UpdateArtifactRequest.SerializeToString,
        response_deserializer=buildstream_dot_buildstream__pb2.UpdateArtifactResponse.FromString,
        )
    self.Status = channel.unary_unary(
        '/buildstream.ArtifactCache/Status',
        request_serializer=buildstream_dot_buildstream__pb2.StatusRequest.SerializeToString,
        response_deserializer=buildstream_dot_buildstream__pb2.StatusResponse.FromString,
        )


class ArtifactCacheServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetArtifact(self, request, context):
    """Retrieve a cached artifact.

    Errors:
    * `NOT_FOUND`: The requested `ActionResult` is not in the cache.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateArtifact(self, request, context):
    """Associate a cache key with a CAS build artifact.

    Errors:
    * `RESOURCE_EXHAUSTED`: There is insufficient storage space to add the
    entry to the cache.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Status(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ArtifactCacheServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetArtifact': grpc.unary_unary_rpc_method_handler(
          servicer.GetArtifact,
          request_deserializer=buildstream_dot_buildstream__pb2.GetArtifactRequest.FromString,
          response_serializer=buildstream_dot_buildstream__pb2.GetArtifactResponse.SerializeToString,
      ),
      'UpdateArtifact': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateArtifact,
          request_deserializer=buildstream_dot_buildstream__pb2.UpdateArtifactRequest.FromString,
          response_serializer=buildstream_dot_buildstream__pb2.UpdateArtifactResponse.SerializeToString,
      ),
      'Status': grpc.unary_unary_rpc_method_handler(
          servicer.Status,
          request_deserializer=buildstream_dot_buildstream__pb2.StatusRequest.FromString,
          response_serializer=buildstream_dot_buildstream__pb2.StatusResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'buildstream.ArtifactCache', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
