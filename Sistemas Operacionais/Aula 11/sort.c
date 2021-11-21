/*
 * Copyright(C) 2011-2016 Pedro H. Penna <pedrohenriquepenna@gmail.com>
 * 
 * This file is part of Nanvix.
 * 
 * Nanvix is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 * 
 * Nanvix is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with Nanvix. If not, see <http://www.gnu.org/licenses/>.
 */
 
#include <sys/stat.h>
#include <sys/types.h>
#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/* Software versioning. */
#define VERSION_MAJOR 1 /* Major version. */
#define VERSION_MINOR 0 /* Minor version. */

/* Program arguments. */
static char *const *filenames; /* Files to concatenate.           */
static int nfiles = 0;         /* Number of files to concatenate. */

typedef struct GetNumberOfLinesResponse {
	int lines;
} GetNumberOfLinesResponse;

static void sortLines(char** input, int lines)
{
	char temp[BUFSIZ];

	int i=0, j=0;

	for(i=0; i<lines; i++){
		for(j=0; j<lines-1-i; j++){
			if(strcmp(input[j], input[j+1]) > 0){
				strcpy(temp, input[j]);
				strcpy(input[j], input[j+1]);
				strcpy(input[j+1], temp);
			}
		}
	}
}

static GetNumberOfLinesResponse getNumberOfLines(char *filename)
{
	GetNumberOfLinesResponse resp = {1};
    int fd;
	char buf[BUFSIZ];
	ssize_t n, nread; 

    fd = open(filename, O_RDONLY);

	if (fd < 0)
	{
		fprintf(stderr, "cat: cannot open %s\n", filename);
		return resp;
	}

	do {
		if ((nread = read(fd, buf, BUFSIZ)) < 0) {
			fprintf(stderr, "cat: cannot read %s\n", filename);
			resp.lines = -1;
			return resp;
		}
		
		n = nread;

		int i = 0;

		while (i < nread) {
			if (buf[i] == '\n') {
				resp.lines++;
			}
			i++;
		}

	} while (n == BUFSIZ);

	close(fd);

    return resp;
}

static void sort(char *filename)
{
    GetNumberOfLinesResponse resp = getNumberOfLines(filename);

	char** fileLines = malloc(resp.lines*sizeof(char*));
	int* breakpoints = malloc((resp.lines+1)*sizeof(int));
	int fd;
	char buf[BUFSIZ];
	ssize_t n, nread; 

    fd = open(filename, O_RDONLY);

	if (fd < 0)
	{
		fprintf(stderr, "cat: cannot open %s\n", filename);
		return;
	}

	breakpoints[0] = 0;
	int i = 0, j= 1;

	/*
	buffer de 10bytes

	eu tenho 15bytes

	n0: 10bytes
	n1: 5bytes

	i tá errado, dar uma olhada dps
	*/
	do {
		if ((nread = read(fd, buf, BUFSIZ)) < 0) {
			fprintf(stderr, "cat: cannot read %s\n", filename);
			return;
		}
		
		n = nread;

		i = 0;
		while (i < nread) {
			if (buf[i] == '\n') {
				breakpoints[j] = i;
				j++;
			}
			i++;
		}

	} while (n == BUFSIZ);

	if (buf[i] != '\n') {
		breakpoints[resp.lines] = i;
	}

	do {
		if ((nread = read(fd, buf, BUFSIZ)) < 0) {
			fprintf(stderr, "cat: cannot read %s\n", filename);
			return;
		}
		
		n = nread;
		
		int i = 0;
		for(i=1; i <= resp.lines; i++) {

			fileLines[i-1] = malloc(BUFSIZ*sizeof(char));

			int j = 0;
			for (j=breakpoints[i-1]; j <= breakpoints[i]; j++) {
				if (buf[j] != '\n'){
					/*dar uma olhada memcpy, remove o uso do \0*/

					char cToStr[2] = {buf[j], '\0'};
					strcat(fileLines[i-1], cToStr);
				}
			}
		}
		
	} while (n == BUFSIZ);

	sortLines(fileLines, resp.lines);
	
	int k = 0;
	for(k=0; k < resp.lines; k++) {
		printf("%s\n", fileLines[k]);
	}

	/*FREE do Malloc*/

	close(fd);

	for(k=0; k < resp.lines; k++) {
		free(fileLines[k]);
	}

	free(fileLines);
	free(breakpoints);
}

static void version(void)
{
	printf("cat (Nanvix Coreutils) %d.%d\n\n", VERSION_MAJOR, VERSION_MINOR);
	printf("Copyright(C) 2011-2014 Pedro H. Penna\n");
	printf("This is free software under the "); 
	printf("GNU General Public License Version 3.\n");
	printf("There is NO WARRANTY, to the extent permitted by law.\n\n");
	
	exit(EXIT_SUCCESS);
}

static void usage(void)
{
	printf("Usage: cat [options] [files]\n\n");
	printf("Brief: Concatenates files.\n\n");
	printf("Options:\n");
	printf("  --help    Display this information and exit\n");
	printf("  --version Display program version and exit\n");
	
	exit(EXIT_SUCCESS);
}

static void getargs(int argc, char *const argv[])
{
	int i;     
	char *arg; 
	
	for (i = 1; i < argc; i++)
	{
		arg = argv[i];
		
		if (!strcmp(arg, "--help"))
			usage();
		
		else if (!strcmp(arg, "--version"))
			version();
		
		else
		{
			if (nfiles++ == 0)
				filenames = &argv[i];
		}
	}
}

int main(int argc, char *const argv[])
{	
	int i;         
	char *filename;
	struct stat st;
	
	getargs(argc, argv);
	
	if (nfiles == 0)
		sort("/dev/tty");
	
	else
	{
		for (i = 0; i < nfiles; i++)
		{
			filename = filenames[i];
			
			if (!strcmp(filename, "-"))
				filename = "/dev/tty";
			
			else
			{
				if (stat(filename, &st) == -1)
				{
					fprintf(stderr, "cat: cannot stat %s\n", filename);
					continue;
				}
				
				/* File is directory. */
				if (S_ISDIR(st.st_mode))
				{
					fprintf(stderr, "cat: %s is a directory\n", filename);
					continue;
				}
			}
				
			sort(filename);
		}
	}
	
	return(EXIT_SUCCESS);
}
