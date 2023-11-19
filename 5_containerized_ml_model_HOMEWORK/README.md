# Homework: Create a containerized ML model

### Tools:

- docker -> [tutorial](https://docs.docker.com/get-started/02_our_app/)
- flask API -> [python tutorial](https://pythonbasics.org/flask-rest-api/)
- pickle -> [python tutorial](https://pythonarray.com/how-to-pickle-unpickle-tutorial/)

### Task

Use the `model.pkl` containing a python object (ML model) with the method:

```python
.predict(input: NDArray[(Any, 10), float]) -> NDArray[(Any, 1), float]

# Example call:
model.predict([[1,2.65,3,4,5,6.124,7,8,9,10], [1,2,67,4,5,7.065,7,1,9,10]])
# Output: array([175.65822, 175.65822], dtype=float32)
```

It can be loaded using:

```python
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
```

**Remark:** the model needs the `xgboost==1.5.0` library.

Create a docker container with a flask API allowing to query the model.
It should habe two endpoints:

- `GET /ping` returning json `{"ping": "success"}`
- `POST /predict` returning json `{"Result": "<prediction>"}`

```bash
# example cURL
curl \
    -X POST 
    -d '[[1,2.65,3,4,5,6.124,7,8,9,10], [1,2,67,4,5,7.065,7,1,9,10]]' \
    localhost:5000
```
