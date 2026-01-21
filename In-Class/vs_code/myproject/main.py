import httpx

def main() -> None:
    r = httpx.get(
        "https://icanhazdadjoke.com/",
        headers={"Accept": "application/json"},
        timeout=10,
    )
    r.raise_for_status()
    print(r.json()["joke"])

if __name__ == "__main__":
    main()





