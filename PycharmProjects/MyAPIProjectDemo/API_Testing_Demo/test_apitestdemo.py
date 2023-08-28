import requests
ENDPOINT="https://todo.pixegami.io"
# response=requests.get(ENDPOINT)
# print(response)
# data=response.json()
# print(data)
# status_code=response.status_code
# print(status_code)

def create_task(payload):
    return requests.put(ENDPOINT+"/create-task", json=payload)

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def get_task(task_id):
    return  requests.get(ENDPOINT + f"/get-task/{task_id}")

def delete_task(task_id):
    return  requests.delete(ENDPOINT + f"/delete-task/{task_id}")

def new_task_payload():
    return {
        "content": "my_test_content",
        "user_id": "test_user",
        "is_done": False,
    }


def test_to_verify_endpoint_response():
    response=requests.get(ENDPOINT)
    assert response.status_code == 200

def test_to_verify_creation_of_new_resource_api():
    # payload={
    #     "content":"my_test_content",
    #     "user_id":"test_user",
    #     "is_done":False,
    # }
    payload=new_task_payload()
    # create_task_response=requests.put(ENDPOINT+"/create-task", json=payload)
    create_task_response = create_task(payload)
    assert create_task_response.status_code==200
    data=create_task_response.json()
    print(data)

    #we need to know weather the resource which we have created is actually there or not and that
    # can be done by fetching the task_id of newly created resource
    task_id=data["task"]["task_id"]
    # get_task_response=requests.get(ENDPOINT+f"/get-task/{task_id}")
    get_task_response =get_task(task_id)
    assert get_task_response.status_code==200

    #check the content of the Newly created resource weather its matching the actual passed payload
    # content or not
    get_task_data=get_task_response.json()
    print(get_task_data)
    assert get_task_data["content"]==payload["content"]
    assert get_task_data["user_id"]==payload["user_id"]

def test_to_verfy_updation_of_newly_created_api_resource():
    #create new task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id=create_task_response.json()["task"]["task_id"]
    #update the task
    new_payload={
        "user_id":payload["user_id"],
        "task_id":task_id,
        "content": "my updated content",
        "is_done": True,
    }
    update_task_response=update_task(new_payload)
    assert update_task_response.status_code==200

    get_task_response=get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data=get_task_response.json()
    assert get_task_data["content"]==new_payload["content"]
    assert get_task_data["is_done"]==new_payload["is_done"]

def test_to_validate_deletion_of_api():
    # create new task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    #delete task:
    delete_task_response=delete_task(task_id)
    assert delete_task_response.status_code == 200

    #get the task and check it's not found
    get_task_response=get_task(task_id)
    print(get_task_response.status_code)
    assert get_task_response.status_code == 404



