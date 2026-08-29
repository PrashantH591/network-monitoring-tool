import socket
import time
from datetime import datetime


TARGETS = [
    ("google.com", 443),
    ("cloudflare.com", 443),
]


def check_target(host, port, timeout=5):
    start_time = time.perf_counter()

    try:
        ip_address = socket.gethostbyname(host)

        with socket.create_connection(
            (host, port),
            timeout=timeout
        ):
            pass

        response_time = (time.perf_counter() - start_time) * 1000

        return {
            "host": host,
            "port": port,
            "ip": ip_address,
            "status": "PASS",
            "response_ms": round(response_time, 2),
        }

    except socket.gaierror:
        return {
            "host": host,
            "port": port,
            "ip": "N/A",
            "status": "DNS FAILED",
            "response_ms": None,
        }

    except OSError:
        return {
            "host": host,
            "port": port,
            "ip": "N/A",
            "status": "CONNECTION FAILED",
            "response_ms": None,
        }


def generate_report(results):
    report = []
    report.append("=" * 55)
    report.append("NETWORK MONITORING REPORT")
    report.append("=" * 55)
    report.append(
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    report.append("")

    for result in results:
        report.append(f"Host: {result['host']}")
        report.append(f"Port: {result['port']}")
        report.append(f"IP Address: {result['ip']}")
        report.append(f"Status: {result['status']}")

        if result["response_ms"] is not None:
            report.append(
                f"Response Time: {result['response_ms']} ms"
            )

        report.append("-" * 55)

    return "\n".join(report)


def main():
    results = []

    for host, port in TARGETS:
        result = check_target(host, port)
        results.append(result)

    print(generate_report(results))


if __name__ == "__main__":
    main()
