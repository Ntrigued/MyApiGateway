This project is a Django-based API Gateway for routing to various services. It exists to gate access to various API accounts I want users of my website to have access to.

It works in a pretty standard way:
- Each user may have an account on my site.
- They send a request to the gateway
- The gateway checks if the user has access to the service requested
  - if so, it makes the call to the requested service and returns the result
  - otherwise, it sends back something like a 401