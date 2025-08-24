from concurrent import futures
import grpc  

import course_service_pb2  # Сгенерированные классы для работы с gRPC-сообщениями
import course_service_pb2_grpc # Сгенерированный класс для работы с сервисом


class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    """Реализация методов gRPC-сервиса CourseService"""

    def GetCourse(self, request, context):
        """Метод GetCourse обрабатывает входящий запрос"""
        print(f'Получен запрос к методу GetCourse c id : {request.course_id}')

        # Формируем и возвращаем ответное сообщение
        return course_service_pb2.GetCourseResponse(
            course_id=request.course_id,  # из запроса
            title="Автотесты API",        # всегда эта строка
            description="Будем изучать написание API автотестов",  # всегда эта строка
            message=f"{request.course_id},{request.title}, {request.description}"
        )
    
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