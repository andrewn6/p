<script lang="ts">
  export let width: number = 15;
  export let height: number = 10;
  let color: [number, number, number][] = [
    [281, 100, 52],
    [266, 100, 52],
  ];

  const SCALE = 2;
  const RADIUS = 3;

  type Pos = { x: number; y: number };
  let i = 0,
    j = 0;
  let dotPos = { x: width - RADIUS - 1, y: height / 2 };
  let previousPositions: Pos[] = [];

  function lerp(start: number, end: number, amt: number) {
    return (1 - amt) * start + amt * end;
  }

  function hsl([h, s, l]: [number, number, number]) {
    return `hsl(${h}, ${s}%, ${l}%)`;
  }

  function frame(ctx: CanvasRenderingContext2D) {
    // at the beginning, make sure we are using updated width/height data
    if (i === 0) dotPos = { x: width - RADIUS - 1, y: height / 2 };
    i += 0.01;
    j = Math.sin(i) * 20;
    previousPositions.unshift({ ...dotPos });
    if (previousPositions.length > width - RADIUS * 2 - 1) {
      previousPositions.length = width - RADIUS * 2 - 1;
    }
    dotPos.y = height / 2 + Math.sin(i + j) * (height / 2 - RADIUS - 1);
    draw(ctx);
    requestAnimationFrame(() => frame(ctx));
  }

  function circle(
    ctx: CanvasRenderingContext2D,
    { x, y }: Pos,
    radius: number,
    color: string
  ) {
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, 2 * Math.PI);
    ctx.fillStyle = color;
    ctx.fill();
  }

  function draw(ctx: CanvasRenderingContext2D) {
    ctx.clearRect(0, 0, width, height);
    circle(ctx, dotPos, RADIUS, hsl(color[0]));
    for (const [i, { x, y }] of previousPositions.entries()) {
      let invertedI = previousPositions.length - i;
      const currentColor = color[0].map((component, i) =>
        lerp(component, color[1][i], invertedI / previousPositions.length)
      ) as [number, number, number];
      circle(ctx, { x: x - i, y }, RADIUS, hsl(currentColor));
    }
  }

  function beginAnimation(canvas: HTMLCanvasElement) {
    let ctx = canvas.getContext("2d") as CanvasRenderingContext2D;
    // Scale canvas for better resolution

    canvas.style.width = width + "px";
    canvas.style.height = height + "px";
    canvas.width = width * SCALE;
    canvas.height = height * SCALE;

    width = width * SCALE;
    height = height * SCALE;

    requestAnimationFrame(() => frame(ctx));
  }
</script>

<div>
  <canvas use:beginAnimation />
</div>

<style>
  div {
    display: inline-block;
  }
</style>
