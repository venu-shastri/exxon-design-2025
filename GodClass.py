import pyodbc

class TradeRecord:
    def __init__(self, source_currency, destination_currency, lots, price):
        self.source_currency = source_currency
        self.destination_currency = destination_currency
        self.lots = lots
        self.price = price


class TradeProcessor:
    LOT_SIZE = 100000.0

    def process_trades(self, stream):
        # --- Read lines from stream ---
        lines = [line.strip() for line in stream if line.strip()]

        trades = []
        line_count = 1

        for line in lines:
            fields = line.split(",")

            if len(fields) != 3:
                print(f"WARN: Line {line_count} malformed. Only {len(fields)} field(s) found.")
                line_count += 1
                continue

            if len(fields[0]) != 6:
                print(f"WARN: Trade currencies on line {line_count} malformed: '{fields[0]}'")
                line_count += 1
