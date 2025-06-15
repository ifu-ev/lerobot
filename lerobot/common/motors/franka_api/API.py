# flake8: noqa
import grpc
import lerobot.common.motors.franka_api.franka_api_pb2 as franka_api_pb2
import lerobot.common.motors.franka_api.franka_api_pb2_grpc as franka_api_pb2_grpc


class API:
    def __init__(self, server_address):
        self.channel = grpc.insecure_channel(server_address)
        self.stub = franka_api_pb2_grpc.FrankaServiceStub(self.channel)

    def get_joint_state(self):
        js = self.stub.GetJointState(franka_api_pb2.Empty())
        return js
    
    def get_joint_position(self):
        js = self.stub.GetJointState(franka_api_pb2.Empty())
        return js.position
    
    def get_wrench(self):
        wrench = self.stub.GetWrench(franka_api_pb2.Empty())
        return wrench
    
    def get_cart_pose(self):
        cartpose = self.stub.GetEEFPose(franka_api_pb2.Empty())
        return cartpose
    
    def set_joint_position(self, position):
        response = self.stub.SetJointTarget(franka_api_pb2.JointState(
            name=["panda_joint1", "panda_joint2", "panda_joint3", "panda_joint4", "panda_joint5", "panda_joint6", "panda_joint7"],
            position=list(position)
        ))
        return response.message

    def set_cart_pose(self, pose):

        if len(pose) == 3:
            position_to_send = pose

            current_pose_obj = self.get_cart_pose()
            print(current_pose_obj)
            orientation_to_send = [
                current_pose_obj.qx,
                current_pose_obj.qy,
                current_pose_obj.qz,
                current_pose_obj.qw
            ]

            
            response = self.stub.SetCartPoseTarget(franka_api_pb2.Pose(
                x = position_to_send[0],
                y = position_to_send[1],
                z = position_to_send[2],
                qx = orientation_to_send[0],
                qy = orientation_to_send[1],
                qz = orientation_to_send[2],
                qw = orientation_to_send[3],
            ))
            return response.message    
            
        elif len(pose) == 7:
            response = self.stub.SetCartPoseTarget(franka_api_pb2.Pose(
            x = pose[0],
            y = pose[1],
            z = pose[2],
            qx = pose[3],
            qy = pose[4],
            qz = pose[5],
            qw = pose[6],
        ))
            return response.message 
        else:
            raise ValueError(f"Invalid Pose")
        
        # response = self.stub.SetCartPoseTarget(franka_api_pb2.Pose(
        #     x = position_to_send[0],
        #     y = position_to_send[1],
        #     z = position_to_send[2],
        #     qx = orientation_to_send[3],
        #     qy = orientation_to_send[4],
        #     qz = orientation_to_send[5],
        #     qw = orientation_to_send[6],
        # ))
        # return response.message    
    