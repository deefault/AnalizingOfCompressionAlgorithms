#include <stdio.h>
#include <limits.h>
#include <errno.h>


int RleEncodeFile(char *in, char *out)
{
    int currChar;
    int prevChar;
    unsigned char count;
    FILE *inFile=NULL;
    FILE *outFile=NULL;
    if(in)
    {
        inFile = fopen(in, "rb");
    }

    if(out)
    {
        outFile = fopen(out, "wb");
    }

    if ((NULL == inFile) || (NULL == outFile))
    {
        errno = ENOENT;
        return -1;
    }

    prevChar = EOF;
    count = 0;

    while ((currChar = fgetc(inFile)) != EOF)
    {
        fputc(currChar, outFile);
        if (currChar == prevChar)
        {
            count = 0;
            while ((currChar = fgetc(inFile)) != EOF)
            {
                if (currChar == prevChar)
                {
                    count++;
                    if (count == UCHAR_MAX)
                    {
                        fputc(count, outFile);
                        prevChar = EOF;
                        break;
                    }
                }
                else
                {
                    fputc(count, outFile);
                    fputc(currChar, outFile);
                    prevChar = currChar;
                    break;
                }
            }
        }
        else
        {
            prevChar = currChar;
        }

        if (currChar == EOF)
        {
            fputc(count, outFile);
            break;
        }
    }
    fclose(outFile);
    return 0;
}


int RleDecodeFile(char *in, char *out)
{
    int currChar;
    int prevChar;
    unsigned char count;

    FILE *inFile=NULL;
    FILE *outFile=NULL;
    if(in)
    {
        inFile = fopen(in, "rb");
    }

    if(out)
    {
        outFile = fopen(out, "wb");
    }

    if ((NULL == inFile) || (NULL == outFile))
    {
        errno = ENOENT;
        return -1;
    }

    prevChar = EOF;

    while ((currChar = fgetc(inFile)) != EOF)
    {
        fputc(currChar, outFile);
        if (currChar == prevChar)
        {
            count = fgetc(inFile);
            while (count > 0)
            {
                fputc(currChar, outFile);
                count--;
            }
            prevChar = EOF;
        }
        else
        {
            prevChar = currChar;
        }
    }
    return 0;
}
