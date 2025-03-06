# Unittests in JS

## Description  
This project focuses on learning JavaScript's queueing system. It manages tasks or data in a specific order.

## Learning Objectives
By the end of this project, you should be able to:
 - How to run a Redis server on your machine
 - How to run simple operations with the Redis client
 - How to use a Redis client with Node JS for basic operations
 - How to store hash values in Redis
 - How to deal with async operations with Redis
 - How to use Kue as a queue system
 - How to build a basic Express app interacting with a Redis server
 - How to the build a basic Express app interacting with a Redis server and queue

## Requirements
 - All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
 - All of your files should end with a new line
 - A README.md file, at the root of the folder of the project, is mandatory
 - Your code should use the js extension

## Tasks

### 0. Install a Redis instance
- Download, extract, and compile the latest stable Redis version.

### 1. Node Redis Client
- Install `node_redis` using npm.
- Create `0-redis_client.js` to connect to the Redis server.
  - Log `Redis client connected to the server` on successful connection.
  - Log `Redis client not connected to the server: ERROR_MESSAGE` on failure.

### 2. Node Redis Client and Basic Operations
- Copy `0-redis_client.js` into `1-redis_op.js`.
- Implement:
  - `setNewSchool(schoolName, value)`: Stores a key-value pair in Redis and logs confirmation using `redis.print`.
  - `displaySchoolValue(schoolName)`: Logs the value of the given key.

### 3. Node Redis Client and Async Operations
- Copy `1-redis_op.js` into `2-redis_op_async.js`.
- Modify `displaySchoolValue` to use `async/await` with `promisify`.

### 4. Node Redis Client and Advanced Operations
- Create `4-redis_advanced_op.js` to store and retrieve hash values.
- Use `hset` to store a hash under the key `HolbertonSchools`:
  - `Portland=50`, `Seattle=80`, `New York=20`, `Bogota=20`, `Cali=40`, `Paris=2`.
- Use `hgetall` to display the stored hash.

### 5. Node Redis Client Publisher and Subscriber
- Create:
  - `5-subscriber.js`:
    - Logs connection status.
    - Subscribes to `holberton school channel`.
    - Logs received messages and exits on `KILL_SERVER`.
  - `5-publisher.js`:
    - Logs connection status.
    - Implements `publishMessage(message, time)`, which sends messages to `holberton school channel` after a delay.

### 6. Create the Job Creator
- Create `6-job_creator.js`:
  - Uses Kue to create a job queue `push_notification_code`.
  - Logs job creation, completion, and failure statuses.

### 7. Create the Job Processor
- Create `6-job_processor.js`:
  - Uses Kue to process jobs from `push_notification_code`.
  - Implements `sendNotification(phoneNumber, message)` to log notifications.

### 8. Track Progress and Errors with Kue: Job Creator
- Create `7-job_creator.js`:
  - Stores job data in an array.
  - Creates jobs in `push_notification_code_2`.

### 9. Track Progress and Errors with Kue: Job Processor
- Create `7-job_processor.js`:
  - Maintains a blacklist of phone numbers.
  - Implements `sendNotification(phoneNumber, message, job, done)`.
  - Tracks job progress and fails jobs for blacklisted numbers.

### 10. Writing the Job Creation Function
- Create `8-job.js`:
  - Implements `createPushNotificationsJobs(jobs, queue)`.
  - Throws an error if `jobs` is not an array.
  - Logs job progress, completion, and failures.

### 11. Writing the Test for Job Creation
- Write tests for `createPushNotificationsJobs`:
  - Use Kue’s `testMode` to verify jobs in the queue.

### 12. In Stock?
- Create an array `listProducts` with product details.
- Implement `getItemById(id)` to retrieve products.
- Set up an Express server in `9-stock.js` (port `1245`).
- Implement `GET /list_products` to return all products in JSON format.


**Repository:**  
GitHub: `atlas-web_back_end`  
Directory: `queuing_system_in_js`  

## Author
[Jesse Brumley](https://github.com/jessebrumley)
