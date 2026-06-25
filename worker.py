import json

from app.redis_client import r
from app.database import SessionLocal
from app.models import TelemetryEvent

print("🚀 Telemetry Worker Started...")

while True:

    item = r.brpop("telemetry_queue")

    event = json.loads(item[1])

    db = SessionLocal()

    try:

        telemetry = TelemetryEvent(
            agent_name=event["agent_name"],
            event_type=event["event_type"],
            latency=event["latency"],
            tokens=event["tokens"],
            cost_usd=event["cost_usd"],
            workflow_id=event["workflow_id"],
            status=event["status"],
            message=event["message"]
        )

        db.add(telemetry)

        db.commit()

        print(
            f"✅ Stored: "
            f"{event['agent_name']} | "
            f"{event['event_type']} | "
            f"{event['workflow_id']}"
        )

    except Exception as e:

        print(f"❌ Error: {e}")

        db.rollback()

    finally:

        db.close()