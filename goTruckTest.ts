//// Question 1

interface DigitRandomGenerator {

    generateDigit: () => number

}

class MyDigitRandomGenerator implements DigitRandomGenerator { 
    
    generateDigit = () => {

        // ** METHOD 1 **  

        // const findCeil = (arr: any[], r: number, l: number, h: number) => {
        //     let mid: number;
        //     while (l < h)
        //     {
        //         mid = l + ((h - l) >> 1); // Same as mid = (l+h)/2
        //         (r > arr[mid]) ? (l = mid + 1) : (h = mid);
        //     }
        //     return (arr[l] >= r) ? l : -1;
        // }
        
        // let arr: number[] = []
        // for (let w = 1; w <= 10; w++) {
        //     arr.push(w)
        // }
     
        // const n = arr.length
        // let freq: number[] = []
        // for (let w = 1; w <= 10; w++) {
        //     freq.push((10**10)*(10**10))
        // }
     

        // let prefix= [];
        // let i: number;
        // prefix[0] = freq[0];
        // for (i = 1; i < n; ++i)
        //     prefix[i] = prefix[i - 1] + freq[i];
 
        // // prefix[n-1] is sum of all frequencies.
        // // Generate a random number with
        // // value from 1 to this sum
        // let r = Math.floor((Math.random()* prefix[n - 1])) + 1;
 
        // // Find index of ceiling of r in prefix array
        // let indexc = findCeil(prefix, r, 0, n - 1);
        // const value_to_return = arr[indexc]
        // return value_to_return;
       
        // ** METHOD 2 **
        var num=Math.random();
        if(num < 0.1) return 1; 
        else if(num < 0.2) return 2;
        else if(num < 0.3) return 3;
        else if(num < 0.4) return 4;
        else if(num < 0.4) return 4;
        else if(num < 0.5) return 5;
        else if(num < 0.6) return 6;
        else if(num < 0.7) return 7;
        else if(num < 0.8) return 8;
        else if(num < 0.9) return 9;
        else return 10;


    }

}

// ** Check result of question 1 solution **
// var myDigitRandGen = new MyDigitRandomGenerator()
// for (let i = 1; i <= 100; i ++) {
//     console.log(myDigitRandGen.generateDigit())
// }


//// Question 2a 
/*

Possible causes: 
a. When an exception is unrecognized (is neither HttpException nor a class that inherits from HttpException), a JSON response with a http status code of 500 would be thrown
b. There was no query string orderID passed in from the client request. Could be a misspelling or typo
c. An order is not found with the stated orderID
d. An exception is thrown during the update operation

*/

// Question 2b
/*

Possible improvements: 
1. Wrap the body of the cancelOrder method in a try catch block. In the catch block, throw InternalServerErrorException and console log the error 
2. First, check if there is 'orderID' in query string, otherwise throw new BadRequestException("Invalid order ID")
3. Before checking (order.isCancelled), check if (order === null) { throw new UnprocessableEntityException() }
4. Await the response from the update operation, e.g. await this.prisma.purchaseOrder.update... ; return "success" only after the update operation has been completed successfully, 
   so that in the event of a server/database error or network error that causes the update to fail to perform, the client will be notified with the appropriate status code, and corresponding action can be taken such as to retry at another time.

*/

// Question 2c
/*

- Perform validation testing 
1. a request with valid order ID that had not been cancelled prior - expected response "status 200, success"
2. a request with valid order ID that had been cancelled previously - expected response "status 400, message: Order is not active"
3. a request without query string "orderID" - expected response (based on the improvements in 2b) "status 400, message: Invalid order ID"
4. a request with order ID properly formed but non-existing order based on it - expected response (based on the improvements in 2b) "status 422"
5. simulate server error but killing the server or cutting off connection with the database - expected response "status 500, Internal server error"

*/



