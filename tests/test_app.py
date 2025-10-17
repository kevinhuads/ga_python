from app.main import main

def test_main_default():
    assert main('world') == 'Hello from Python app, world!'

def test_main_custom():
    assert main('CI') == 'Hello from Python app, CI!'   