# Use a lightweight web server image
FROM nginx:alpine

# Remove default HTML
RUN rm -rf /usr/share/nginx/html/*

# Copy our static HTML into Nginx folder
COPY index.html /usr/share/nginx/html

# Expose port 80 for access
EXPOSE 80

# Start Nginx (default command works)
