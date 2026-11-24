"""줄 단위 프로토콜 도우미 (3교시 LAB 3 완성본). 수정하지 않습니다."""
import socket

ENCODING = "utf-8"


def send_line(sock: socket.socket, text: str) -> None:
    sock.sendall((text.replace("\n", " ") + "\n").encode(ENCODING))


class LineReader:
    def __init__(self, sock: socket.socket, bufsize: int = 1024):
        self.sock = sock
        self.bufsize = bufsize
        self.buffer = b""

    def read_line(self) -> str | None:
        while b"\n" not in self.buffer:
            data = self.sock.recv(self.bufsize)
            if not data:
                return None
            self.buffer += data
        line, self.buffer = self.buffer.split(b"\n", 1)
        return line.decode(ENCODING, errors="replace").rstrip("\r")