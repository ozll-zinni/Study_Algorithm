function solution(sequence, k) {
  let n = sequence.length;
  let start = 0;
  let sum = 0;

  let bestStart = 0;
  let bestEnd = 0;
  let minLength = Infinity; 
  
  for (let end = 0; end < n; end++) {
    sum += sequence[end];
    
    while (sum >= k) {
      if (sum === k) {
        let length = end - start + 1;
        
        if (length < minLength) {
          minLength = length;
          bestStart = start;
          bestEnd = end;
        }
        else if (length === minLength && start < bestStart) {
          bestStart = start;
          bestEnd = end;
        }
      }
      
      sum -= sequence[start];
      start++;
    }
  }
  
  return [bestStart, bestEnd];
}
