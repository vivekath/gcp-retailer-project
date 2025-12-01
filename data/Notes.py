CLUSTER_NAME="my-demo-cluster2"
REGION="us-east1"

gcloud dataproc clusters create ${CLUSTER_NAME} \
  --region=${REGION} \
  --num-workers=2 \
  --worker-machine-type=n1-standard-2 \
  --worker-boot-disk-size=50 \
  --master-machine-type=n1-standard-2 \
  --master-boot-disk-size=50 \
  --image-version=2.0-debian10 \
  --enable-component-gateway \
  --optional-components=JUPYTER \
  --initialization-actions=gs://goog-dataproc-initialization-actions-${REGION}/connectors/connectors.sh \
  --metadata bigquery-connector-version=1.2.0,spark-bigquery-connector-version=0.21.0



# Setting SQL instance => 4. Lecture 2: Setting up the Data sources – SQL DBs, GCS, BQ, Configs => 9:53 / 43:13
# mockapi.io => used for dummy API's => 4. Lecture 2: Setting up the Data sources – SQL DBs, GCS, BQ, Configs => 31:53 / 43:13
# create bucket => 5. Lecture 3 : Configuring Google Cloud Storage (GCS) as a landing zone => 1:44 / 9:12
# Create dataproc cluster => 6. Lecture 4: Data Ingestion - Dataproc, Pyspark, GCS Landing-Session1 => 0:51 / 1:27:38
# Silver layer, null, duplicate, scd(2) incr, full load (truncate&load)
# Setting Cloud Compose => 12. Lecture 10: Setting up Airflow DAGS for workflow orchestration => 1:45 / 27:54
# Cloud compose bucket => 12. Lecture 10: Setting up Airflow DAGS for workflow orchestration => 16:25 / 27:54
# Setting Cloud Build trigger CICD => 13. Lecture 11: complete CICD with Github, cloud build and airflow => 21:34 / 1:03:14


