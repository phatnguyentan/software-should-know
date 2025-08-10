A **Distributed Denial of Service (DDoS)** attack is a malicious attempt to disrupt the normal functioning of a targeted server, service, or network by overwhelming it with a flood of internet traffic. In a DDoS attack, multiple compromised computer systems (often part of a botnet) are used to send a high volume of requests to the target, exhausting its resources and making it unavailable to legitimate users.

### Key Characteristics of DDoS Attacks

- **Volume-Based Attacks**: These include UDP floods and ICMP floods, which aim to saturate the bandwidth of the target.
- **Protocol Attacks**: These exploit weaknesses in network protocols, such as SYN floods, which consume server resources.
- **Application Layer Attacks**: These target specific applications, like HTTP floods, aiming to crash the web server.

### Preventing DDoS Attacks in Express.js

While it's difficult to completely prevent DDoS attacks, you can implement several strategies in an Express.js application to mitigate their impact. Here are some common techniques:

1. **Rate Limiting**: Limit the number of requests from a single IP address over a specific time period.

2. **IP Whitelisting/Blacklisting**: Allow or deny access based on IP addresses.

3. **Using a CDN**: Content Delivery Networks (CDNs) can absorb and distribute traffic load.

4. **Traffic Analysis**: Monitor traffic patterns to detect anomalies.

5. **Web Application Firewalls (WAF)**: Use WAFs to filter out malicious traffic.

### Example: Rate Limiting in Express.js

Here’s a simple example of how to implement rate limiting in an Express.js application using the `express-rate-limit` middleware:

```javascript
const express = require('express');
const rateLimit = require('express-rate-limit');

const app = express();

// Create a rate limiter
const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100, // Limit each IP to 100 requests per windowMs
    message: 'Too many requests, please try again later.'
});

// Apply the rate limiter to all requests
app.use(limiter);

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
```

### Explanation of the Code

1. **Import Modules**: The code imports the Express framework and the `express-rate-limit` middleware.

2. **Create an Express Application**: An instance of the Express application is created.

3. **Define Rate Limiter**:
   - `windowMs`: Sets the time window for requests (15 minutes in this case).
   - `max`: Defines the maximum number of requests allowed from a single IP within the time window.
   - `message`: Custom message returned when the limit is exceeded.

4. **Apply Rate Limiter**: The rate limiter is applied globally to all incoming requests.

5. **Define a Route**: A simple route is defined that responds with "Hello, World!".

6. **Start the Server**: The application listens on port 3000.

### Conclusion

DDoS attacks can significantly disrupt services, but with proper strategies like rate limiting, you can mitigate their effects. While the example provided is a basic implementation, in a production environment, you should consider more comprehensive solutions, including using CDNs, WAFs, and traffic monitoring tools to enhance security and resilience against DDoS attacks.