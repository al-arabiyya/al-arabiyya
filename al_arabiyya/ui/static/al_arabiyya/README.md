# UI Styles

Basic commands to get started.

First `cd` into dir:

```console
cd al_arabiyya/ui/static/al_arabiyya
```

To generate the styles:

```console
npm install
cd al_arabiyya/ui/static/al_arabiyya
npx @tailwindcss/cli -i ../static/al_arabiyya/css/app.css -o ../static/al_arabiyya/css/styles.css --cwd ../../templates -m -w
```

To format the templates:

```console
npx prettier -w ../../templates
```
