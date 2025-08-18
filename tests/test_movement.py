import vrcosc
import time

def test_jump() -> None:
    vrc = vrcosc.VRCOSC()
    vrc.jump()
    time.sleep(2)
