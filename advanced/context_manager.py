class DatabaseConnection:
    def __enter__(self):
        self.connection = self._connect_to_db()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def _connect_to_db(self):
        class Connection:
            def close(self):
                print("connection closed")

        return Connection()


def main():
    with DatabaseConnection() as conn:
        print("using db connection")


if __name__ == "__main__":
    main()
