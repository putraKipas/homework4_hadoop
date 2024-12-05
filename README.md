## Instalasi

1. **Instal Hadoop**: Pastikan Anda telah menginstal Hadoop pada mesin Anda (macos).
   - $ brew install hadoop
   - $ cd /opt/homebrew/Cellar/hadoop/3.3.6/libexec/etc/hadoop
2. **Konfigurasi Hadoop**: Edit file konfigurasi seperti `core-site.xml`, `hdfs-site.xml` dan `mapred-site.xml` untuk menjalankan Hadoop dalam _standalone mode_.
3. **Konfigurasi Test Hadoop**:
   - $ hadoop namenode -format
   - $ start-all.sh
4. **Persiapkan File Input**: Pastikan file `pembukaan_uud1945.txt` tersedia di direktori yang tepat.
5. **Persiapkan Mapper dan Reducer**:
   - `mapper.py`: Skrip ini akan memetakan kata-kata dari input file dan memberikan output pasangan kata dan jumlah kemunculannya.
   - `reducer.py`: Skrip ini akan menerima hasil mapper dan menggabungkan hasilnya untuk menghitung total kemunculan setiap kata.

## Cara Menjalankan

### 1. Menjalankan Hadoop Streaming Job

Setelah Anda mengonfigurasi Hadoop dan mempersiapkan file input (`pembukaan_uud1945.txt`), Anda dapat menjalankan job Hadoop menggunakan perintah berikut:

hadoop jar "%HADOOP_HOME%\share\hadoop\tools\lib\hadoop-streaming-3.2.3.jar" \
 -mapper "python mapper.py" \
 -reducer "python reducer.py" \
 -input /usr/doc/hadoop_wordcount_project/input/pembukaan_uud1945.txt \
 -output output

atau jika ingin line:
hadoop jar "%HADOOP_HOME%\share\hadoop\tools\lib\hadoop-streaming-3.2.3.jar" -mapper "python mapper.py" -reducer "python reducer.py" -input /usr/doc/hadoop_wordcount_project/input/pembukaan_uud1945.txt -output output

## Memeriksa Hasil Output

hadoop fs -ls output

hadoop fs -cat output/part-00000

hadoop fs -rm -r output # Membersihkan output
