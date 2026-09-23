FROM nixos/nix:latest AS builder

COPY . /build
WORKDIR /build

RUN nix \
	--extra-experimental-features "nix-command flakes" \
	build .

RUN mkdir /build/nix-store-closure
RUN cp -R $(nix-store -qR /build/result) /build/nix-store-closure

# ---

FROM scratch

WORKDIR /app
COPY --from=builder /build/nix-store-closure /nix/store
COPY --from=builder /build/result /app

CMD [ "/app/bin/pywebview-react-app" ]
