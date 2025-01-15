import json
from services.crawler import crawl_builder
from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from services.socket import ConnectionManager
manager = ConnectionManager()
router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    user_unique_id = await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)
            user_state = manager.get_user_state(user_unique_id)
            if not user_state:
                await manager.send_message(unique_id=user_unique_id,
                                           message=f"Starting To Crawl FOR {data['url']}")
                manager.modify_user_state(user_unique_id, "crawling")
                crawler = crawl_builder(data['url'], data['crawlType'])
                web_content = await crawler.crawl()
                await manager.send_message(unique_id=user_unique_id, message=f"Crawling Done\
                                                                             Contents Are \n\n"
                                                                             f"{web_content}")
                # manager.modify_user_state(user_unique_id, "")
                manager.send_message(user_unique_id, "Disconncting YOU NOW")
                manager.disconnect(user_unique_id)

            else:
                await manager.send_message(unique_id=user_unique_id, message="Please Be Patient")
    except WebSocketDisconnect:
        await manager.disconnect(user_unique_id)
