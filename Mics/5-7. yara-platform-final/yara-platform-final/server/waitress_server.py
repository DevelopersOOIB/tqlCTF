from waitress import serve
import yara_platform
serve(yara_platform.app, host='0.0.0.0', port=80)