HTML_PAGE = """

<!DOCTYPE html>
<html>
<head>
<title>Pico W Robot Car</title>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
/* =================== BASE =================== */
body {
    margin: 0;
    height: 100vh;
    font-family: Arial;
}

/* Lock portrait */
@media (orientation: portrait) {
    body::before {
        content: "Rotate phone to landscape";
        position: fixed;
        inset: 0;
        background: black;
        color: white;
        font-size: 28px;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 999;
    }
}

/* =================== CONTAINERS =================== */
.left-container {
    position: fixed;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.right-container {
    position: fixed;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
}

.speed-container {
    position: fixed;
    right: 280px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* =================== SPEED SLIDER =================== */
.speed-slider {
    writing-mode: bt-lr;
    -webkit-appearance: slider-vertical;
    width: 40px;
    height: 250px;
}

.speed-label {
    margin-top: 10px;
    font-size: 16px;
}

/* =================== STEERING =================== */
.steer-grid {
    display: grid;
    grid-template-columns: 110px 110px;
    grid-template-rows: 70px 70px;
    gap: 15px;
    justify-items: center;
    align-items: center;
}

.btn-middle {
    grid-column: 1 / 3;
    justify-self: center;
}

/* =================== BUTTONS =================== */
button {
    width: 110px;
    height: 70px;
    font-size: 18px;
    border: none;
    border-radius: 12px;
    background: #2563eb;
    color: white;
}

button:active {
    background: #1e40af;
}
</style>
</head>

<body>

<!-- =================== STEERING =================== -->
<div class="right-container">
    <div class="steer-grid">
        <button class="btn-middle" onclick="steer('middle')">MIDDLE</button>
        <button onclick="steer('left')">LEFT</button>
        <button onclick="steer('right')">RIGHT</button>
    </div>
</div>

<!-- =================== SPEED =================== -->
<div class="speed-container">
    <input
        type="range"
        min="0"
        max="100"
        value="33"
        class="speed-slider"
        oninput="setSpeed(this.value)">
    <div class="speed-label">Speed</div>
</div>

<!-- =================== DRIVE =================== -->
<div class="left-container">
    <button
        onmousedown="drive('forward')"
        onmouseup="drive('stop')"
        ontouchstart="drive('forward')"
        ontouchend="drive('stop')"
        ontouchcancel="drive('stop')">
        Forward
    </button>

    <button
        onmousedown="drive('backward')"
        onmouseup="drive('stop')"
        ontouchstart="drive('backward')"
        ontouchend="drive('stop')"
        ontouchcancel="drive('stop')">
        Backward
    </button>
</div>

<script>
function steer(dir) {
    fetch("/steer?dir=" + dir);
}

function drive(dir) {
    fetch("/trajectory?dir=" + dir);
}

function setSpeed(value) {
    fetch("/speed?value=" + value);
}
</script>

</body>
</html>



"""

