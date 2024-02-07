import datetime
from flask import request
from extensions import app, db
from models import Result


def formatEvent(event):
    return {
        "id": event.id,
        "description": event.description,
        "created_at": event.created_at,
    }


@app.route("/events", methods=["POST"])
def create_event():
    description = request.json["description"]
    event = Result(description=description)
    db.session.add(event)
    db.session.commit()
    return formatEvent(event)


@app.route("/events", methods=["GET"])
def get_events():
    events = Result.query.all()
    return {"events": list(map(formatEvent, events))}


@app.route("/events/<int:id>", methods=["GET"])
def get_events_for_date(id):
    event = Result.query.filter_by(id=id).one()
    if event:
        return {"events": formatEvent(event)}
    else:
        return {"error": "event not found"}


@app.route("/events/update/<int:id>", methods=["PUT"])
def update_event(id):
    event = Result.query.filter_by(id=id).one()
    event.description = request.json["description"]
    event.created_at = datetime.datetime.utcnow()
    db.session.commit()
    return formatEvent(event)


@app.route("/events/delete/<int:id>", methods=["DELETE"])
def delete_event(id):
    event = Result.query.filter_by(id=id).one()
    db.session.delete(event)
    db.session.commit()
    return {"deleted event": id}


if __name__ == "__main__":
    app.run()
