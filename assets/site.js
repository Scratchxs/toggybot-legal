const motion = matchMedia('(prefers-reduced-motion: reduce)');
let lenis;
function configureMotion() {
  lenis?.destroy();
  lenis = undefined;
  if (!motion.matches && typeof Lenis !== 'undefined') {
    lenis = new Lenis({ autoRaf: true, anchors: true, duration: 1.05 });
  }
}
configureMotion();
motion.addEventListener('change', configureMotion);
