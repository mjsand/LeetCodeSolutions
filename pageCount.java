class Result {

    /*
     * Complete the 'pageCount' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER p
     */

    public static int pageCount(int n, int p) {
        int pagesForward = 0;
        int pagesBackward = 0;
        
        pagesForward = Math.floorDiv(p, 2);
        
        if (n % 2 == 0){
            pagesBackward = Math.floorDiv(n-p+1, 2);
        }
        else {
            pagesBackward = Math.floorDiv(n-p, 2);
        }
        if (pagesForward < pagesBackward){
            return pagesForward;
        }
        else {
            return pagesBackward;
        }
    }
}