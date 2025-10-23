#! /usr/bin/env sh

# Exit in case of error
set -e
#pip install openapi-python-client

for service in auth-users deals; do # api-gateway-service plans-service proposals-service chat-service; do
  folder=fro-$service-service-client
  folder2="fro_$(echo "$service" | tr '-' '_')_service_client"
  rm -rf ./src/corelib/services/$folder2
  rm -rf $folder
  openapi-python-client generate --url "http://$service:8000/api/v1/openapi.json"
  mv $folder/$folder2 ./src/corelib/services
  rm -rf $folder
done