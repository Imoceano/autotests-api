import asyncio 
import websockets  
from websockets import ServerConnection



async def echo(websocket: ServerConnection):
    async for message in websocket:  
        print(f"Получено сообщение: {message}") 
        response = f"Сервер получил: {message}" # Формируем ответное сообщение
        await websocket.send(f"1 Сообщение пользователя: {message}")
        await websocket.send(f"2 Сообщение пользователя: {message}")
        await websocket.send(f"3 Сообщение пользователя: {message}") 
        await websocket.send(f"4 Сообщение пользователя: {message}") 
        await websocket.send(f"5 Сообщение пользователя: {message}") 


# Запуск WebSocket-сервера на порту 8765
async def main():
    server = await websockets.serve(echo, "localhost", 8765)  # Запускаем сервер
    print("WebSocket сервер запущен на ws://localhost:8765")  # Выводим сообщение о запуске
    await server.wait_closed() # Ожидаем закрытия сервера (обычно он работает вечно)


asyncio.run(main())