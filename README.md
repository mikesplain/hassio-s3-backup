[![hacs_badge](https://img.shields.io/badge/HACS-Custom-blue.svg)](https://github.com/hacs/integration)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/mikesplain/hassio-s3-backup)](https://github.com/mikesplain/hassio-s3-backup/releases)
[![GitHub](https://img.shields.io/github/license/mikesplain/hassio-s3-backup)](LICENSE)
[![Validate](https://github.com/mikesplain/hassio-s3-backup/actions/workflows/validate.yml/badge.svg)](https://github.com/mikesplain/hassio-s3-backup/actions/workflows/validate.yml)

# Home Assistant Generic S3 Backup

A Home Assistant custom integration that enables storing and managing Home Assistant backups on any S3-compatible object storage provider (e.g., Cloudflare R2, Wasabi, MinIO, DigitalOcean Spaces, and more). This is an alternative to the built-in AWS S3 integration, supporting a wider range of providers.

---

## Features

- Upload Home Assistant backups to S3-compatible storage
- Restore backups directly from your S3 bucket
- Tested with Cloudflare R2 (other providers should work if S3 API compatible)
- Easy configuration via the Home Assistant UI

---

## Installation

### HACS (Recommended)
1. In Home Assistant, go to **HACS > Integrations**.
2. Click the three dots (⋮) in the top right and choose **Custom repositories**.
3. Add this repository URL and select **Integration** as the category.
4. Search for `Generic S3 Backup` in HACS and install.
5. Restart Home Assistant.

### Manual
1. Download this repository as a ZIP file and extract.
2. Copy the `custom_components/hassio_s3_backup` folder into your Home Assistant `custom_components` directory.
3. Restart Home Assistant.

---

## Configuration

1. In Home Assistant, go to **Settings > Devices & Services > Integrations**.
2. Click **Add Integration** and search for `Generic S3 Backup`.
3. Enter the following details for your S3-compatible provider:
   - **Access Key ID**: Your S3 API access key
   - **Secret Access Key**: Your S3 API secret
   - **Bucket Name**: The name of your bucket (must exist and be writable)
   - **Endpoint URL**: The provider’s S3 endpoint (e.g., `https://<accountid>.r2.cloudflarestorage.com` for Cloudflare R2)
4. Complete the setup. The integration will verify your credentials and bucket access.

---

## Usage

- Backups created in Home Assistant will be uploaded to your S3 bucket automatically.
- You can restore backups directly from the S3 bucket via the Home Assistant UI.
- All backup management (list, download, delete) is available through the standard Home Assistant backup interface.

---

## Troubleshooting

- **Cannot connect to endpoint**: Double-check your endpoint URL and network connectivity.
- **Invalid credentials**: Ensure your access key and secret are correct and have permissions for the bucket.
- **Invalid bucket name**: The bucket must already exist and be writable by the provided credentials.

Check Home Assistant logs for detailed error messages.

---

## Supported Providers

- Cloudflare R2 (tested)
- Any provider supporting the S3 API (Wasabi, DigitalOcean Spaces, MinIO, etc.)

If you successfully use another provider, please open an issue or PR to update this list!

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Credits

Created by [mikesplain](https://github.com/mikesplain). Inspired by the Home Assistant integration blueprint and AWS S3 backup integration.

---

## Need Help?

Open an issue on the [GitHub repository](https://github.com/mikesplain/hassio-s3-backup/issues) for support or feature requests.
