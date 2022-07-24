# -*- coding: utf-8 *-*

import uvicorn


def run_api():
    uvicorn.run('api.core:api', host='0.0.0.0', port=8080, reload=True)


if __name__ == '__main__':
    run_api()

