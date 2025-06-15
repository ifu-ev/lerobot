# flake8: noqa
import grpc
import lerobot.common.motors.uf850_api.uf850_api_pb2 as uf850_api_pb2
import lerobot.common.motors.uf850_api.uf850_api_pb2_grpc as uf850_api_pb2_grpc


class API:
    def __init__(self, server_address):
        self.channel = grpc.insecure_channel(server_address)
        self.stub = uf850_api_pb2_grpc.Uf850ServiceStub(self.channel)

    def get_joint_state(self):
        js = self.stub.GetJointState(uf850_api_pb2.Empty())
        return js
    
    def get_joint_position(self):
        js = self.stub.GetJointState(uf850_api_pb2.Empty())
        return js.position
    
    def get_wrench(self):
        wrench = self.stub.GetWrench(uf850_api_pb2.Empty())
        return wrench
    
    def get_cart_pose(self):
        cartpose = self.stub.GetEEFPose(uf850_api_pb2.Empty())
        return cartpose
    
    def set_joint_position(self, position):
        response = self.stub.SetJointTarget(uf850_api_pb2.JointState(
            name=["panda_joint1", "panda_joint2", "panda_joint3", "panda_joint4", "panda_joint5", "panda_joint6", "panda_joint7"],
            position=list(position)
        ))
        return response.message
    
    