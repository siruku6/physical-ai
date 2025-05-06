import time

import pybullet as p
import pybullet_data
from PIL import Image

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -10)

planeId = p.loadURDF("plane.urdf")
startPos = [0, 0, 1]
startOrientation = p.getQuaternionFromEuler([0, 0, 0])
boxId = p.loadURDF("r2d2.urdf", startPos, startOrientation)

# シミュレーションステップ
for i in range(240):
    p.stepSimulation()
    time.sleep(1.0 / 240.0)

# カメラの位置と向きの設定
viewMatrix = p.computeViewMatrix(
    cameraEyePosition=[1, 1, 1],
    cameraTargetPosition=[0, 0, 0],
    cameraUpVector=[0, 0, 1],
)
# カメラのビューの設定
projectionMatrix = p.computeProjectionMatrixFOV(
    fov=60, aspect=1.0, nearVal=0.1, farVal=100.0
)

# カメラ画像を取得
width, height, rgbImg, depthImg, segImg = p.getCameraImage(
    width=512, height=512, viewMatrix=viewMatrix, projectionMatrix=projectionMatrix
)
img = Image.fromarray(rgbImg)
img.save("screenshot.png")
p.disconnect()
