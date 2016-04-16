import json
import pickle

if __name__ == '__main__':
    d = {'aaa': 0, 'bbb': 1, 'ccc': 2}
    with open('pickling.dat', 'wb') as f:
        pickle.dump(d, f)

    with open('pickling.dat', 'rb') as f:
        d2 = pickle.load(f)
        print(d2)

    print(json.dumps(d))
