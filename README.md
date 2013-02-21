A python script to recursively copy directories. 

I needed to selectively copy files from one directory to another, and I needed to preserve the original directory structure. However, I wanted to filter out unwanted file types, so I wanted to be able to specify a "primary" file type that would mark any enclosing directory for copying, and a variable sized list of "secondary" file types that would also be copied across. I didn't wany any files that did not match one of the specified file extensions to be copied. 

If my bash-fu was stronger, maybe this could all have been done with a couple of lines of shell script. And I suppose I could have just recursively copied over all directories from the root of the source, or else all directories containing a primary file type, and then executed a second bash command to recursively delete the unwanted ones. However, I tend to reach for python once anything I am trying to do in the shell moves beyond a pretty basic level of complexity. 

Runtime parameters are:
.txt /home/mf/scratch/source /home/mf/scratch/target .xml
<primary file type> <source directory> <target directory> <secondary file types list>
