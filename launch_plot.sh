for folder in ${experiments}/* ; do
  python plot.py experiments/ $folder
done