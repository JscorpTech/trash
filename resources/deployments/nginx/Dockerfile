# Dockerfile for Nginx
FROM nginx:1.27-alpine-slim

# Remove the default NGINX configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy your custom NGINX configuration file into the container
COPY .resources/deployments/nginx/nginx.conf /etc/nginx/conf.d/default.conf