import httpx 
from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient


class GetExersiseQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий.
    """
    courseId: str

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создания заданий.
    """
    title: str
    courseId: str
    max_score: int
    min_score: int
    orderIndex:int | None
    description: str
    estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление заданий.
    """
    title: str
    max_score: int
    min_score: int
    orderIndex:int | None
    description: str
    estimatedTime: str



    

class  ExercisesClient(APIClient):


    def get_list_of_exercises_api(self, query: GetExersiseQueryDict ) -> Response:
        """
        Метод получения списка заданий на курсе по course_id выбранного курса.

        :param query: Словарь с course_id.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        
        return self.get(f"http://localhost:8000/api/v1/exercises", params=query)
    
    def get_exercise_api(self, exercise_id: str) -> Response:

        """
        Метод получения выбранного курса по exercise_id.
        param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
    
        """
        return self.get (f"http://localhost:8000/api/v1/exercises/{exercise_id}")
    
    def create_exersise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания записи задания.

        :param request: Словарь с обязательными полями tittle, courseId, max_score, min_score, description, estimatedTime и необязательным полем orderIndex.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.post(f"http://localhost:8000/api/v1/exercises", json=request)
    
    def update_exersise_api(self, exercise_id:str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод  обновления записи задания.

        :param request: Словарь с обязательными полями tittle, max_score, min_score, description, estimatedTime и необязательным полем orderIndex.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.patch (f"http://localhost:8000/api/v1/exercises/{exercise_id}", json=request)
    
   
    
    def delete_exercise_api(self,exercise_id: str) -> Response:
        """
        Метод удаления выбранного задания по exercise_id.
        param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
    
        """

        return self.delete (f"http://localhost:8000/api/v1/exercises/{exercise_id}")