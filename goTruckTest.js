// Question 1
var MyDigitRandomGenerator = /** @class */ (function () {
    function MyDigitRandomGenerator() {
        this.generateDigit = function () {
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
            var num = Math.random();
            if (num < 0.1)
                return 1; //probability 0.3
            else if (num < 0.2)
                return 2; // probability 0.3
            else if (num < 0.3)
                return 3; //probability 0.3
            else if (num < 0.4)
                return 4; //probability 0.3
            else if (num < 0.4)
                return 4; //probability 0.3
            else if (num < 0.5)
                return 5; //probability 0.3
            else if (num < 0.6)
                return 6; //probability 0.3
            else if (num < 0.7)
                return 7; //probability 0.3
            else if (num < 0.8)
                return 8; //probability 0.3
            else if (num < 0.9)
                return 9; //probability 0.3
            else
                return 10; //probability 0.1
        };
    }
    return MyDigitRandomGenerator;
}());
var myDigitRandGen = new MyDigitRandomGenerator();
for (var i = 1; i <= 100; i++) {
    console.log(myDigitRandGen.generateDigit());
}
// console.log(myDigitRandGen.generateDigit())
