from __future__ import annotations

import json
from flask import Flask, jsonify, request
from pydantic import (
    BaseModel,
    EmailStr,
    ValidationError,
    Field,
    field_validator,
    ValidationInfo,
)

app = Flask(__name__)


class Address(BaseModel):
    city: str = Field(..., min_length=2)
    street: str = Field(..., min_length=3)
    house_number: int = Field(..., ge=1)


class User(BaseModel):
    name: str = Field(..., min_length=2)
    age: int = Field(..., ge=0, le=120)
    email: EmailStr | None = None
    is_employed: bool | None = None
    address: Address | None = None

    @field_validator("is_employed")
    def validate_is_employed(
        cls, v: bool | None, info: ValidationInfo
    ) -> bool | None:
        """
        Пользователь младше 18 лет не может быть трудоустроен.
        """
        age = info.data.get("age")
        if age is not None and age < 18 and v:
            raise ValueError("Users under 18 years old cannot be employed")
        return v


@app.route("/register", methods=["POST"])
def create_user():
    """
    HTTP-эндпоинт для регистрации пользователя.
    """
    data = request.get_json()
    try:
        user = User(**data)
        return jsonify({"message": "User created successfully", "user": user.model_dump()})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400


if __name__ == "__main__":
    # Пример JSON для локальной проверки без запуска сервера
    json_input = """
    {
        "name": "John Doe",
        "age": 70,
        "email": "john.doe@example.com",
        "is_employed": true,
        "address": {
            "city": "New York",
            "street": "5th Avenue",
            "house_number": 123
        }
    }
    """

    try:
        user = User(**json.loads(json_input))
        print("User created successfully:")
        print(user.model_dump())
    except ValidationError as e:
        print("Validation error:", e.errors())