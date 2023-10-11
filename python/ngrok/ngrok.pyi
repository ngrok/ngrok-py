# See API documentation for full information on the available functions:
# https://ngrok.github.io/ngrok-python/

def connect(
    addr: Union[None, str, int] = None,
    listener: Optional[Listener] = None,
    **options: object,
) -> Listener: ...
def default(session: Optional[Session] = None) -> Listener: ...
def disconnect(url: Optional[str] = None) -> None: ...
def fd(session: Optional[Session] = None) -> int: ...
def getsockname(session: Optional[Session] = None) -> str: ...
def kill() -> None: ...
def listen(
    server: Optional[Any] = None, listener: Optional[Listener] = None
) -> Listener: ...
def log_level(level: str = "INFO") -> None: ...
def pipe_name() -> str: ...
def werkzeug_develop(
    listener: Optional[Listener] = None,
) -> Union[Awaitable[Listener], Listener]: ...

class Listener:
    def close(self) -> Awaitable[None]: ...
    def forward(self, addr: str) -> Awaitable[None]: ...
    def forwards_to(self) -> str: ...
    def id(self) -> str: ...
    def labels(self) -> Mapping[str, str]: ...
    def metadata(self) -> str: ...
    def proto(self) -> str: ...
    def url(self) -> str: ...

class Session:
    def close(self) -> Awaitable[None]: ...
    def close_listener(self, id: str) -> Awaitable[None]: ...
    def get_listeners(self) -> List[Listener]: ...
    def http_endpoint(self) -> HttpListenerBuilder: ...
    def labeled_endpoint(self) -> LabeledListenerBuilder: ...
    def tcp_endpoint(self) -> TcpListenerBuilder: ...
    def tls_endpoint(self) -> TlsListenerBuilder: ...

class SessionBuilder:
    def authtoken(self, authtoken: str) -> SessionBuilder: ...
    def authtoken_from_env(self) -> SessionBuilder: ...
    def ca_cert(self, cert_bytes: bytearray) -> SessionBuilder: ...
    def client_info(
        self, client_type: str, version: str, comments: Optional[str] = None
    ) -> SessionBuilder: ...
    def connect(self) -> Awaitable[Session]: ...
    def handle_disconnection(self, handler: Callable[[str, str]]) -> SessionBuilder: ...
    def handle_heartbeat(self, handler: Callable[[int]]) -> SessionBuilder: ...
    def handle_restart_command(self, handler: Callable[[]]) -> SessionBuilder: ...
    def handle_stop_command(self, handler: Callable[[]]) -> SessionBuilder: ...
    def handle_update_command(
        self, handler: Callable[[str, str]]
    ) -> SessionBuilder: ...
    def heartbeat_interval(self, heartbeat_interval: int) -> SessionBuilder: ...
    def heartbeat_tolerance(self, heartbeat_tolerance: int) -> SessionBuilder: ...
    def metadata(self, metadata: str) -> SessionBuilder: ...
    def server_addr(self, server_addr: str) -> SessionBuilder: ...

class HttpListenerBuilder:
    def allow_cidr(self, cidr: str) -> HttpListenerBuilder: ...
    def allow_user_agent(self, regex: str) -> HttpListenerBuilder: ...
    def basic_auth(self, username: str, password: str) -> HttpListenerBuilder: ...
    def circuit_breaker(self, circuit_breaker: float) -> HttpListenerBuilder: ...
    def compression(self) -> HttpListenerBuilder: ...
    def deny_cidr(self, cidr: str) -> HttpListenerBuilder: ...
    def deny_user_agent(self, regex: str) -> HttpListenerBuilder: ...
    def domain(self, domain: str) -> HttpListenerBuilder: ...
    def forwards_to(self, forwards_to: str) -> HttpListenerBuilder: ...
    def listen(self) -> Awaitable[Listener]: ...
    def listen_and_forward(self, url: str) -> Awaitable[Listener]: ...
    def listen_and_serve(self, server: Any) -> Awaitable[Listener]: ...
    def metadata(self, metadata: str) -> HttpListenerBuilder: ...
    def mutual_tlsca(self, mutual_tlsca: bytearray) -> HttpListenerBuilder: ...
    def oauth(
        self,
        provider: str,
        allow_emails: Optional[list[str]] = None,
        allow_domains: Optional[list[str]] = None,
        scopes: Optional[list[str]] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
    ) -> HttpListenerBuilder: ...
    def oidc(
        self,
        issuer_url: str,
        client_id: str,
        client_secret: str,
        allow_emails: Optional[list[str]] = None,
        allow_domains: Optional[list[str]] = None,
        scopes: Optional[list[str]] = None,
    ) -> HttpListenerBuilder: ...
    def proxy_proto(self, proxy_proto: str) -> HttpListenerBuilder: ...
    def remove_request_header(self, name: str) -> HttpListenerBuilder: ...
    def remove_response_header(self, name: str) -> HttpListenerBuilder: ...
    def request_header(self, name: str, value: str) -> HttpListenerBuilder: ...
    def response_header(self, name: str, value: str) -> HttpListenerBuilder: ...
    def scheme(self, scheme: str) -> HttpListenerBuilder: ...
    def webhook_verification(
        self, provider: str, secret: str
    ) -> HttpListenerBuilder: ...
    def websocket_tcp_conversion(self) -> HttpListenerBuilder: ...

class LabeledListenerBuilder:
    def label(self, label: str, value: str) -> LabeledListenerBuilder: ...
    def listen(self) -> Awaitable[Listener]: ...
    def listen_and_forward(self, url: str) -> Awaitable[Listener]: ...
    def listen_and_serve(self, server: Any) -> Awaitable[Listener]: ...
    def metadata(self, metadata: str) -> LabeledListenerBuilder: ...

class TcpListenerBuilder:
    def allow_cidr(self, cidr: str) -> TcpListenerBuilder: ...
    def deny_cidr(self, cidr: str) -> TcpListenerBuilder: ...
    def forwards_to(self, forwards_to: str) -> TcpListenerBuilder: ...
    def listen(self) -> Awaitable[Listener]: ...
    def listen_and_forward(self, url: str) -> Awaitable[Listener]: ...
    def listen_and_serve(self, server: Any) -> Awaitable[Listener]: ...
    def metadata(self, metadata: str) -> TcpListenerBuilder: ...
    def proxy_proto(self, proxy_proto: str) -> TcpListenerBuilder: ...
    def remote_addr(self, remote_addr: str) -> TcpListenerBuilder: ...

class TlsListenerBuilder:
    def allow_cidr(self, cidr: str) -> TlsListenerBuilder: ...
    def deny_cidr(self, cidr: str) -> TlsListenerBuilder: ...
    def domain(self, domain: str) -> TlsListenerBuilder: ...
    def forwards_to(self, forwards_to: str) -> TlsListenerBuilder: ...
    def listen(self) -> Awaitable[Listener]: ...
    def listen_and_forward(self, url: str) -> Awaitable[Listener]: ...
    def listen_and_serve(self, server: Any) -> Awaitable[Listener]: ...
    def metadata(self, metadata: str) -> TlsListenerBuilder: ...
    def mutual_tlsca(self, mutual_tlsca: bytearray) -> TlsListenerBuilder: ...
    def proxy_proto(self, proxy_proto: str) -> TlsListenerBuilder: ...
    def termination(
        self, cert_pem: bytearray, key_pem: bytearray
    ) -> TlsListenerBuilder: ...
