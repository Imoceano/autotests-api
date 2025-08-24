from concurrent import futures
import grpc  

import course_service_pb2  
import course_service_pb2_grpc


class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    """Реализация методов gRPC-сервиса CourseService"""

    def GetCourse(self, request, context):
        """Метод GetCourse обрабатывает входящий запрос"""
        print(f'Получен запрос к методу GetCourse c id : {request.course_id}')

        response = course_service_pb2.GetCourseResponse()
        response.course_id = request.course_id  
        response.title = "Автотесты API" 
        response.description = "Будем изучать написание API автотестов" 
        response.message = f"{request.course_id}, Автотесты API, Будем изучать написание API автотестов"
        
        print(f"Отправляемый ответ: course_id={response.course_id}, title={response.title}, descpition={response.description}")
        return response

    
def serve():
    """Функция создает и запускает gRPC-сервер"""

    # Создаем сервер с использованием пула потоков (до 10 потоков)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Регистрируем сервис UserService на сервере
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)

    # Настраиваем сервер для прослушивания порта 50051
    server.add_insecure_port('[::]:50051')

    # Запускаем сервер
    server.start()
    print("gRPC сервер запущен на порту 50051...")

    # Ожидаем завершения работы сервера
    server.wait_for_termination()


# Запуск сервера при выполнении скрипта
if __name__ == "__main__":
    serve()