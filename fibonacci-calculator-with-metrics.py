import os

from prometheus_client import Gauge, Summary, Counter, start_http_server

fib_calc_duration_seconds = Summary("fib_calc_duration_seconds", "Duration of next fibonacci number in seconds.")
fib_overall_duration_seconds = Summary("fib_overall_duration_seconds", "Overall duration each calc iteration in seconds.")
fib_numbers_total = Counter("fib_numbers_total", "Total Fibonacci numbers printed.", ("user",))
fib_number = Gauge("fib_number", "Current Fibonacci number.", ("user",))


@fib_calc_duration_seconds.time()
def fib(n):
    if n < 0:
        raise ValueError(f"{n} < 0")

    if n < 2:
        return n

    return fib(n-1) + fib(n-2)


def main():
    start_http_server(8800)
    n = 0
    while 1:
        with fib_overall_duration_seconds.time():
            n += 1
            f = fib(n)
            print(f"{f}", flush=True)
            fib_numbers_total.labels(user=os.environ.get("USER")).inc()
            fib_number.labels(user=os.environ.get("USER")).set(f)


if __name__ == "__main__":
    main()
