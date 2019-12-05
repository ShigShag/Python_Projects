import pickle

msg = "wasd"
msg = pickle.dumps(msg)
print(pickle.loads(msg))